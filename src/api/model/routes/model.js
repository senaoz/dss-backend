module.exports = {
  routes: [
    {
      method: "POST",
      path: "/model",
      handler: "model.model",
      config: {
        policies: [],
        middlewares: [],
      },
    },
  ],
};
