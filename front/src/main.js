const forma_authentication = document.querySelector ('.forma-authentication')
const forma_regestration   = document.querySelector ('.forma-regestration')

const authentication_link = 'http://127.0.0.1:3000/authentication';
const regestration_link   = 'http://127.0.0.1:3000/regestration';
const query = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
}

if (forma_authentication)
    forma_authentication.addEventListener ('submit', authentication);
if (forma_regestration)
    forma_regestration.addEventListener ('submit', regestration);

function jwt_decode (token) 
{
    if (!token || typeof token !== "string") throw new Error("Invalid token: must be a non-empty string");
    const base64Url = token.split(".")[1];
    return JSON.parse( atob(base64Url) );
}


async function authentication (event)
{
    event.preventDefault();

    const data = {
        'username': forma_authentication.username.value,
        'email': forma_authentication.emailadr.value,
        'password': forma_authentication.password.value
    }
    query.body = JSON.stringify (data);

    try 
    {
        const response = await fetch (authentication_link, query);
        const result   = await response.json ();

        if (result) 
        {
            const decoded = jwt_decode (result.access_token);
            localStorage.setItem( 'token', result.access_token );
            console.log( 'JWT декодирован:', decoded );

            if (decoded.name == data.username)
                console.log ('Добро пожаловать!');
        }
    } 
    catch (error) 
    { 
        console.error('Ошибка:', error); 
    }
}

async function regestration (event)
{
    event.preventDefault();
    
    const data = {
        'username': forma_regestration.username.value,
        'email': forma_regestration.emailadr.value,
        'password': forma_regestration.password.value
        // 'password': atob (forma_regestration.password.value)
    }
    query.body = JSON.stringify (data);
    
    try 
    {
        const response = await fetch (regestration_link, query);
        const result   = await response.json ();
        console.log ('Успех:', result);
    } 
    catch (error) 
    { 
        console.error('Ошибка:', error); 
    }
}