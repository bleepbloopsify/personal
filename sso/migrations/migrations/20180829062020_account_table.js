
exports.up = function(knex, Promise) {
  return Promise.all([
    knex.schema.createTable('accounts', t => {
  
    }),
  ]);
};

exports.down = function(knex, Promise) {
  return Promise.all([
    knex.schema.dropTable('accounts'),
  ]);
};
