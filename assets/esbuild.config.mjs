import * as esbuild from 'esbuild'
import copyStaticFiles from 'esbuild-copy-static-files'

let minify = false
let sourcemap = true
let watch = true

if (process.env.NODE_ENV === 'production') {
  minify = true
  sourcemap = false
  watch = false
}

const config = {
  entryPoints: ['./js/app.js'],
  outfile: '../public/js/app.js',
  bundle: true,
  minify: minify,
  sourcemap: sourcemap,
  plugins: [copyStaticFiles()],
  external: ['buffer', 'stream', 'assert'], // Adiciona os módulos externos aqui
  platform: 'browser', // Certifique-se de que a plataforma é o browser
}

if (watch) {
  let context = await esbuild.context({ ...config, logLevel: 'info' })
  await context.watch()
} else {
  esbuild.build(config)
}
