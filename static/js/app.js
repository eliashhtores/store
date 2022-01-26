const http = new EasyHTTP()
const server = 'http://localhost:8000/api/v1'

document.querySelector('#login').addEventListener('click', () => {
    const firebaseConfig = {
        apiKey: "AIzaSyBcQZ6c4ML_5RTgySlkNXh0u5NWPMZersk",
        authDomain: "django-store-13768.firebaseapp.com",
        projectId: "django-store-13768",
        storageBucket: "django-store-13768.appspot.com",
        messagingSenderId: "235487373531",
        appId: "1:235487373531:web:13aec099c0e420cace84fe"
    }
    firebase.initializeApp(firebaseConfig)
    const provider = new firebase.auth.GoogleAuthProvider()

    firebase.auth()
        .signInWithPopup(provider)
        .then((result) => {
            /** @type {firebase.auth.OAuthCredential} */
            const user = result.user
            user.getIdToken()
                .then((idToken) => {
                    const data = {
                        'token_id': idToken
                    }
                    http.post(`${server}/user/login`, data)
                        .then((response) => {
                            console.log(response)
                        }).catch((error) => {
                            console.error(error)
                        })
                }).catch((error) => {
                    console.error(error)
                })
        }).catch((error) => {
            console.error(error)
        })
})