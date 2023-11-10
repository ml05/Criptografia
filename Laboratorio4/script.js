// ==UserScript==
// @name         decrypt-lab4
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  no description
// @author       MAguilera
// @match        https://cripto.tiiny.site
// @match        https://brown-rianon-33.tiiny.site
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js
// ==/UserScript==

(function() {
    'use strict';

    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js';
    script.integrity = 'sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==';
    script.crossOrigin = 'anonymous';
    document.head.appendChild(script);


    function decrypt(encryptedMessage, key) {

        // Decodificar el mensaje cifrado en base64
        const ciphertext = CryptoJS.enc.Base64.parse(encryptedMessage);

        // Convertir la clave de texto plano a formato WordArray
        const keyBytes = CryptoJS.enc.Utf8.parse(key);

        // Configurar los parámetros del algoritmo 3DES
        const options = { mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7 };

        // Descifrar el mensaje utilizando 3DES
        const decrypted = CryptoJS.TripleDES.decrypt(
            { ciphertext: ciphertext },
            keyBytes,
            options
        );

        // Devolver el mensaje descifrado como una cadena de texto
        return decrypted.toString(CryptoJS.enc.Utf8);
    }

    // Obtener todo el texto de la pagina
    const texto = document.body.innerText;

    // Dividir el texto en oraciones
    const oraciones = texto.split(/[.!?]+/);

    // Variable para almacenar el primer char de cada oracion
    let key = '';

    // Recorrer cada oración y obtener el primer caracter
    oraciones.forEach((sentence) => {
        const firstChar = sentence.trim().charAt(0);
        key += firstChar;
    });

    console.log(`La llave es: ${key}`);

    var Ids = document.querySelectorAll('[id]');
    console.log(`Los mensajes cifrados son: ${Ids.length}`);

    // muestra el valor de los atributos "id" en la consola
    Ids.forEach((Id) => {
        const mensaje = decrypt(Id.id, key)
        console.log(Id.id + " " + mensaje)
        const div = document.createElement("div");
    div.textContent = mensaje;
    document.body.appendChild(div);
    });
})();
