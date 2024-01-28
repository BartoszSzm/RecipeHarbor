/*!
* Start Bootstrap - Bare v5.0.9 (https://startbootstrap.com/template/bare)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-bare/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


// Handle API calls
async function APICall(url, method, dataToSend) {

    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataToSend)
    };
    try {
        const response = await fetch(url, options)
        const data = await response.json()
        return data
    } catch (error) {
        console.log(`ERROR: ${error}`)
    }
}
