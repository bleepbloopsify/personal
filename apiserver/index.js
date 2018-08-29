const Koa = require('koa');
const logger = require('koa-logger');

const app = new Koa();

const router = require('./router');

app.use(logger());
app.use(router.routes(), router.allowedMethods());

app.listen(process.env.PORT || 9000);
