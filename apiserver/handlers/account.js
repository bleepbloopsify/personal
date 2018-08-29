const { Account } = require('../controllers');

exports.postSignup = async ctx => {
  await Account.createAccount();
};

