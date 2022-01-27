/** 
 * EasyHTTP Library
 * Library for making HTTP requests
 * 
 * @version 3.0.0
 * @author Elías Torres
 * @license MIT
 * 
 **/

// @@ TODO: Get token from LocalStorage
class EasyHTTP {
    // Make an HTTP GET Request
    async get(url) {
        const response = await fetch(url, {
            method: 'GET',
            headers: { 'Authorization': 'Token fe207526177977cfc9f5453c48c6bcfc040f35f5' },
        })
        const resData = await response.json()
        return resData
    }

    // Make an HTTP POST Request
    async post(url, data) {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-type': 'application/json',
                'Authorization': 'Token fe207526177977cfc9f5453c48c6bcfc040f35f5'
            },
            body: JSON.stringify(data)
        })
        const resData = await response.json()
        return resData
    }

    // Make an HTTP PATCH Request
    async patch(url, data) {
        const response = await fetch(url, {
            method: 'PATCH',
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Token fe207526177977cfc9f5453c48c6bcfc040f35f5'
            },
            body: JSON.stringify(data)
        })
        const resData = await response.json()
        return resData
    }

    // Make an HTTP PUT Request
    async put(url, data) {
        const response = await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Token fe207526177977cfc9f5453c48c6bcfc040f35f5'
            },
            body: JSON.stringify(data)
        })
        const resData = await response.json()
        return resData
    }

    // Make an HTTP DELETE Request
    async delete(url) {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-type': 'application/json',
                'Authorization': 'Token fe207526177977cfc9f5453c48c6bcfc040f35f5'
            }
        })
        const resData = await 'Resource deleted'
        return resData
    }

}