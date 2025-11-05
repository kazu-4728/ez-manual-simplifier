import { existsSync, rmSync } from 'node:fs';
import { mkdir } from 'node:fs/promises';
import path from 'node:path';
import { spawn } from 'node:child_process';

async function zipDirectory(sourceDir, zipPath) {
  return new Promise((resolve, reject) => {
    const zipProcess = spawn('zip', ['-r', zipPath, '.'], {
      cwd: sourceDir,
      stdio: ['ignore', 'inherit', 'inherit'],
    });

    zipProcess.on('error', reject);
    zipProcess.on('close', (code) => {
      if (code === 0) {
        resolve(undefined);
      } else {
        reject(new Error(`zip command exited with code ${code}`));
      }
    });
  });
}

async function main() {
  const cwd = process.cwd();
  const resolvedCwd = path.resolve(cwd);
  const isWebDir = path.basename(resolvedCwd) === 'web';
  const projectRoot = isWebDir ? path.dirname(resolvedCwd) : resolvedCwd;
  const webDir = isWebDir ? resolvedCwd : path.join(projectRoot, 'web');
  const outDir = path.join(webDir, 'out');
  const zipPath = path.join(projectRoot, 'site-out.zip');

  if (!existsSync(outDir)) {
    console.error('web/out が見つかりません。`npm run --prefix web export` を先に実行してください。');
    process.exit(1);
  }

  if (existsSync(zipPath)) {
    rmSync(zipPath);
  }

  const outputDir = path.dirname(zipPath);
  if (!existsSync(outputDir)) {
    await mkdir(outputDir, { recursive: true });
  }

  try {
    await zipDirectory(outDir, zipPath);
    const relativeZip = path.relative(projectRoot, zipPath) || path.basename(zipPath);
    console.log(`site-out.zip を作成しました: ${relativeZip}`);
  } catch (error) {
    console.error('site-out.zip の作成に失敗しました。zip コマンドが利用可能か確認してください。');
    console.error(error);
    process.exit(1);
  }
}

main();
