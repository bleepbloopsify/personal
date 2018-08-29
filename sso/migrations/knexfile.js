connection = {
  client: process.env.DB_TYPE,
  connection: {
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_DATABASE,
  },
  pool: {
    min: process.env.DB_POOL_MIN || 2,
    max: process.env.DB_POOL_MAX || 10,
  },
};

module.exports = {

  development: {
    ...connection,
    migrations: {
      tableName: 'knex_migrations',
    },
  },

  staging: {
    ...connection,
    migrations: {
      tableName: 'knex_staging_migrations'
    }
  },

  production: {
    ...connection,
    migrations: {
      tableName: 'knex_production_migrations'
    }
  }

};