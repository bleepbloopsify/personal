const Router = require('koa-router');

const { getIndex, account } = require('./handlers');

const router = new Router();

router.get('/', getIndex);
router.get('/account/signup', account.postSignup);

module.exports = router;
