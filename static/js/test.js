const http = new EasyHTTP()
const server = 'http://localhost:8000/api/v1'

http.get(`${server}/product/by_user`)
    .then((response) => {
        console.log(response)
    }).catch((error) => {
        console.error(error)
    })