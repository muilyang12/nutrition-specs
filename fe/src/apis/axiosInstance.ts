import axios from "axios";

const isProd = process.env.NODE_ENV == "production";

export const axiosInstance = axios.create({
  baseURL: isProd ? "http://api.whatgodsays.net/" : "http://127.0.0.1:8000/",
});
