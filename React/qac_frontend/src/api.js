///This setup allows other parts of the application to make API requests to http://localhost:8000 using the api instance with the base URL preconfigured.
import axios from 'axios';

const api= axios.create({
    baseURL: 'http://localhost:8000'
});

export default api;