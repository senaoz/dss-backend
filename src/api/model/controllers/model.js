module.exports = {
  model: async (ctx) => {
    const input = ctx.request.body;
    const inputFeatures = Object.values(input).join(" ");

    const response = await strapi.services.model.predictPrice(inputFeatures);

    ctx.body = response;
  },
};
