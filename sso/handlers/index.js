

async function getIndex(ctx) {
  ctx.body = `<h1>Hello World!</h1>`;
}

module.exports = { getIndex };