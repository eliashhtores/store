const http = new EasyHTTP()
const server = 'http://127.0.0.1:8000/api/v1'

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
            const credential = result.credential
            const token = credential.idToken
            // const user = result.user
        }).catch((error) => {
            // const errorCode = error.code
            // const errorMessage = error.message
            // const email = error.email
            // const credential = error.credential
            console.error(error)
        })
})