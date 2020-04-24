import axios from "axios";

const CSRF_COOKIE_NAME = "pontocsrftoken";
const CSRF_HEADER_NAME = "X-CSRFToken";

export default axios.create({
  xsrfCookieName: CSRF_COOKIE_NAME,
  xsrfHeaderName: CSRF_HEADER_NAME
});
