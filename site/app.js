const NAV_URL = "./config/nav.json";
const DEFAULT_ROUTE = "docs/TASKS_INDEX.md";
const FALLBACK_ROUTE = "docs/PROJECT_REQUIREMENTS.md";

const appState = {
  navItems: [],
  filteredNavItems: [],
  currentRoute: "",
};

const elements = {};

document.addEventListener("DOMContentLoaded", () => {
  elements.navList = document.getElementById("navList");
  elements.searchInput = document.getElementById("searchInput");
  elements.content = document.getElementById("content");
  elements.breadcrumb = document.getElementById("breadcrumb");
  elements.status = document.getElementById("status");

  elements.searchInput.addEventListener("input", handleSearchInput);
  window.addEventListener("hashchange", handleRouteChange);

  initializeNav();
});

async function initializeNav() {
  setStatus("ナビゲーションを読み込んでいます…");
  try {
    const response = await fetch(NAV_URL, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`nav.json の取得に失敗しました (HTTP ${response.status})`);
    }
    const navJson = await response.json();
    appState.navItems = navJson.map((item) => normalizeNavItem(item));
    appState.filteredNavItems = appState.navItems.slice();
    renderNav();
    setStatus("");
    const routeFromHash = parseRouteFromHash(location.hash);
    if (routeFromHash) {
      loadDocument(routeFromHash);
    } else {
      const defaultRoute = determineDefaultRoute();
      if (defaultRoute) {
        navigateTo(defaultRoute, true);
      } else {
        showErrorMessage("表示できるドキュメントがありません。nav.json を確認してください。");
      }
    }
  } catch (error) {
    console.error(error);
    showErrorMessage("ナビゲーションの読み込みに失敗しました。");
    setStatus(String(error));
  }
}

function normalizeNavItem(item) {
  const sourcePath = String(item.path || "").trim();
  const route = normalizeRouteFromSource(sourcePath);
  return {
    title: String(item.title || route || "Untitled"),
    sourcePath,
    route,
  };
}

function normalizeRouteFromSource(path) {
  if (!path) {
    return "";
  }
  const trimmed = path.replace(/^[.]+\//, "");
  return trimmed.replace(/^\.{2}\//, "");
}

function determineDefaultRoute() {
  if (appState.navItems.some((item) => item.route === DEFAULT_ROUTE)) {
    return DEFAULT_ROUTE;
  }
  if (appState.navItems.some((item) => item.route === FALLBACK_ROUTE)) {
    return FALLBACK_ROUTE;
  }
  return appState.navItems.length > 0 ? appState.navItems[0].route : "";
}

function handleSearchInput(event) {
  const keyword = event.target.value.trim().toLowerCase();
  if (!keyword) {
    appState.filteredNavItems = appState.navItems.slice();
  } else {
    appState.filteredNavItems = appState.navItems.filter((item) => {
      const titleMatch = item.title.toLowerCase().includes(keyword);
      const routeMatch = item.route.toLowerCase().includes(keyword);
      return titleMatch || routeMatch;
    });
  }
  renderNav();
}

function renderNav() {
  if (!elements.navList) {
    return;
  }
  elements.navList.innerHTML = "";
  if (appState.filteredNavItems.length === 0) {
    const emptyItem = document.createElement("li");
    emptyItem.className = "nav__item nav__item--empty";
    emptyItem.textContent = "一致するドキュメントがありません";
    elements.navList.appendChild(emptyItem);
    return;
  }

  const fragment = document.createDocumentFragment();
  for (const item of appState.filteredNavItems) {
    const listItem = document.createElement("li");
    listItem.className = "nav__item";
    const link = document.createElement("a");
    link.className = "nav__link";
    link.textContent = item.title;
    link.href = `#/${encodeURI(item.route)}`;
    link.dataset.route = item.route;
    if (item.route === appState.currentRoute) {
      link.classList.add("nav__link--active");
    }
    link.addEventListener("click", (event) => {
      event.preventDefault();
      navigateTo(item.route);
    });
    listItem.appendChild(link);
    fragment.appendChild(listItem);
  }
  elements.navList.appendChild(fragment);
}

function parseRouteFromHash(hash) {
  if (!hash) {
    return "";
  }
  const normalized = hash.replace(/^#\/?/, "");
  return decodeURIComponent(normalized);
}

function navigateTo(route, replace = false) {
  if (!route) {
    return;
  }
  const targetHash = `#/${encodeURI(route)}`;
  if (replace) {
    location.replace(targetHash);
    handleRouteChange();
  } else if (location.hash !== targetHash) {
    location.hash = targetHash;
  } else {
    handleRouteChange();
  }
}

function handleRouteChange() {
  const route = parseRouteFromHash(location.hash);
  if (!route) {
    const defaultRoute = determineDefaultRoute();
    if (defaultRoute) {
      navigateTo(defaultRoute, true);
    }
    return;
  }
  loadDocument(route);
}

async function loadDocument(route) {
  const sourcePath = toSourcePath(route);
  if (!sourcePath) {
    showErrorMessage("ドキュメントのパスを解決できませんでした。");
    return;
  }

  appState.currentRoute = route;
  setStatus("読み込み中…");
  elements.content.setAttribute("aria-busy", "true");
  try {
    const response = await fetch(sourcePath, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`ドキュメントを取得できませんでした (HTTP ${response.status})`);
    }
    const markdownText = await response.text();
    const renderedHtml = marked.parse(markdownText, { mangle: false, headerIds: true });
    const sanitizedHtml = DOMPurify.sanitize(renderedHtml, { USE_PROFILES: { html: true } });
    elements.content.innerHTML = sanitizedHtml;
    document.title = deriveDocumentTitle(route);
    updateBreadcrumb(route);
    setActiveNav(route);
    rewriteRelativeLinks(route);
    setStatus("");
  } catch (error) {
    console.error(error);
    showErrorMessage("ドキュメントの読み込みに失敗しました。");
    setStatus(String(error));
  } finally {
    elements.content.setAttribute("aria-busy", "false");
  }
}

function toSourcePath(route) {
  if (!route) {
    return "";
  }
  if (route.startsWith("../")) {
    return route;
  }
  return `../${route}`;
}

function deriveDocumentTitle(route) {
  const navItem = appState.navItems.find((item) => item.route === route);
  if (navItem) {
    return `${navItem.title} | EZ Manual Simplifier Docs`;
  }
  return `EZ Manual Simplifier Docs - ${route}`;
}

function setStatus(message) {
  if (!elements.status) {
    return;
  }
  elements.status.textContent = message;
}

function showErrorMessage(message) {
  elements.content.innerHTML = `<div class="content__error">${escapeHtml(message)}</div>`;
}

function setActiveNav(route) {
  const links = elements.navList?.querySelectorAll(".nav__link") ?? [];
  for (const link of links) {
    if (link.dataset.route === route) {
      link.classList.add("nav__link--active");
      link.setAttribute("aria-current", "page");
    } else {
      link.classList.remove("nav__link--active");
      link.removeAttribute("aria-current");
    }
  }
}

function updateBreadcrumb(route) {
  if (!elements.breadcrumb) {
    return;
  }
  elements.breadcrumb.innerHTML = "";
  if (!route) {
    return;
  }
  const segments = route.split("/");
  const fragment = document.createDocumentFragment();
  const accumSegments = [];
  segments.forEach((segment, index) => {
    const span = document.createElement("span");
    span.className = "breadcrumb__item";
    const decoded = decodeURIComponent(segment);
    accumSegments.push(segment);
    const partialRoute = accumSegments.join("/");
    const navMatch = appState.navItems.find((item) => item.route === partialRoute);
    if (navMatch && index !== segments.length - 1) {
      const anchor = document.createElement("a");
      anchor.className = "breadcrumb__link";
      anchor.href = `#/${encodeURI(navMatch.route)}`;
      anchor.textContent = decoded;
      anchor.addEventListener("click", (event) => {
        event.preventDefault();
        navigateTo(navMatch.route);
      });
      span.appendChild(anchor);
    } else {
      span.textContent = decoded;
    }
    fragment.appendChild(span);
  });
  elements.breadcrumb.appendChild(fragment);
}

function rewriteRelativeLinks(currentRoute) {
  const anchors = elements.content.querySelectorAll("a[href]");
  if (!anchors.length) {
    return;
  }
  const baseUrl = new URL(currentRoute, "https://example.com/");
  anchors.forEach((anchor) => {
    const href = anchor.getAttribute("href");
    if (!href || href.startsWith("#")) {
      return;
    }
    if (/^[a-zA-Z][a-zA-Z\d+.-]*:/.test(href)) {
      anchor.setAttribute("rel", "noopener noreferrer");
      anchor.setAttribute("target", "_blank");
      return;
    }
    try {
      const resolved = new URL(href, baseUrl);
      if (!resolved.pathname.endsWith(".md")) {
        anchor.href = resolved.toString();
        return;
      }
      const nextRoute = resolved.pathname.replace(/^\//, "");
      anchor.href = `#/${encodeURI(nextRoute)}`;
      anchor.addEventListener("click", (event) => {
        event.preventDefault();
        navigateTo(nextRoute);
      });
    } catch (error) {
      console.warn("リンクの書き換えに失敗しました", href, error);
    }
  });
}

function escapeHtml(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}
