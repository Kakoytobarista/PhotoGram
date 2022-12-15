const mainApiUrl = 'http://0.0.0.0:8000/api'
const headersParams = {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }

export const getAutocompletePeopleName = async function () {
    try {
        let response = await fetch(`${mainApiUrl}/photo/first_names/`, {
                method: 'GET',
                headers: headersParams,
            }
        )
        return await response.json();
    } catch (e) {
        console.log(e)
    }
}
