const esbuild = require('esbuild');
const path = require('path');
const fs = require('fs');

async function testRender() {
  const outfile = path.join(__dirname, 'temp_bundle.cjs');

  // Bundle App for node
  await esbuild.build({
    entryPoints: [path.join(__dirname, 'src', 'App.tsx')],
    bundle: true,
    platform: 'node',
    format: 'cjs',
    outfile: outfile,
    external: ['react', 'react-dom', 'react-router-dom'],
  });

  const React = require('react');
  const ReactDOMServer = require('react-dom/server');
  const { MemoryRouter } = require('react-router-dom');

  const { App } = require(outfile);

  const routes = [
    { name: '1. Dashboard', path: '/' },
    { name: '2. Explorer', path: '/repo/repo_demo_sample/snapshot/c0ffee1234567890abcdef1234567890abcdef12' },
    { name: '3. Knowledge Graph', path: '/graph/repo_demo_sample/snapshot/c0ffee1234567890abcdef1234567890abcdef12' },
    { name: '4. AI Assistant', path: '/assistant/repo_demo_sample/snapshot/c0ffee1234567890abcdef1234567890abcdef12' },
    { name: '5. Change Impact Analysis', path: '/impact/repo_demo_sample/snapshot/c0ffee1234567890abcdef1234567890abcdef12' },
    { name: '6. Reports', path: '/report/repo_demo_sample/qry_sample_01' },
    { name: '7. Evaluation', path: '/evaluation' },
    { name: '8. Settings', path: '/settings' },
  ];

  console.log('Testing React component rendering across all 8 routes...');
  for (const route of routes) {
    const element = React.createElement(
      MemoryRouter,
      { initialEntries: [route.path] },
      React.createElement(App)
    );
    const html = ReactDOMServer.renderToString(element);
    if (!html || html.length < 50) {
      throw new Error(`Route ${route.name} failed to render content.`);
    }
    console.log(`PASS: Rendered ${route.name} (${route.path}) - HTML length: ${html.length} chars`);
  }

  // Cleanup temp bundle
  if (fs.existsSync(outfile)) {
    fs.unlinkSync(outfile);
  }

  console.log('All 8 dashboard routes successfully rendered in React DOM server runtime with zero exceptions.');
}

testRender().catch((err) => {
  console.error('Render test failed:', err);
  process.exit(1);
});
