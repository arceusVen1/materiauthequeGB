import { createFetch, base, accept, parse } from 'http-client'

export const fetch = createFetch(
    base('https://localhost:8000/api'),  // Prefix all request URLs
    accept('application/json'),         // Set "Accept: application/json" in the request headers
    parse('json')                       // Read the response as JSON and put it in response.body
)