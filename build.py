# Genera index.html (PWA) a partir de la versión de Claude
src=open("/home/claude/calorias/balance.html",encoding="utf-8").read()
src=src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','<link rel="manifest" href="manifest.webmanifest">\n<link rel="icon" href="icon-192.png">\n<link rel="apple-touch-icon" href="icon-192.png">\n')
src=src.replace('lsLoad(); makeCamo(); render();','lsLoad(); makeCamo(); render();\nif("serviceWorker" in navigator){navigator.serviceWorker.register("sw.js").catch(()=>{})}\ntry{navigator.storage&&navigator.storage.persist&&navigator.storage.persist()}catch(e){}',1)
head='<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>\n'
i=src.index('</style>')+len('</style>')
open("/home/claude/balance-pwa/index.html","w",encoding="utf-8").write(head+src[:i]+'\n</head><body>'+src[i:]+'\n</body></html>')
