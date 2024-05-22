import axios from "axios";

const isProd = import.meta.env.PROD;

export const axiosInstance = axios.create({
  baseURL: isProd ? "http://api.whatgodsays.net/" : "http://localhost:8000/",
});
