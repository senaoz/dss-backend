"use strict";

/**
 * A set of functions called "actions" for `model`
 */

module.exports = {
  model: async (ctx, next) => {
    try {
      const input = ctx.request.body;
      const inputFeatures = Object.values(input).join(" ");

      const { exec } = require("child_process");

      const result = new Promise((resolve, reject) => {
        exec(
          `python src/api/model/services/model.py ${inputFeatures}`,
          (error, stdout, stderr) => {
            if (error) {
              console.log(`error: ${error.message}`);
              reject(error.message);
            }
            if (stderr) {
              console.log(`stderr: ${stderr}`);
              reject(stderr);
            }
            console.log(`stdout: ${stdout}`);
            resolve(stdout);
          }
        );
      });

      const response = await result;

      ctx.body = response;
    } catch (err) {
      ctx.body = err;
    }
  },
};
