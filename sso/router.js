const Router = require('koa-router');

const { getIndex } = require('./handlers');

const router = new Router();

router.get('/', getIndex);

module.exports = router;
