"use strict";

/*
 * model service
 */

const { createCoreService } = require("@strapi/strapi").factories;
const { exec } = require("child_process");

module.exports = createCoreService("api::model.model", ({ strapi }) => ({
  async predictPrice(inputFeatures) {
    console.log("Input Features:", inputFeatures);

    return new Promise((resolve, reject) => {
      exec(
        `python ./src/api/model/services/model.py ${inputFeatures}`,
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
  },
}));
