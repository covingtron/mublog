export default {
    async fetch(request) {
        const url = new URL(request.url)
        if (url.pathname.startsWith('/api/')) {
            return new Response('mublog api placeholder', {
                headers: {'Content-Type': 'text/plain'},
            })
        }
        return new Response('Not Found', {status: 404})
    },
}
