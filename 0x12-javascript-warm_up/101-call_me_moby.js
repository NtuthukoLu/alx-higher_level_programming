#!/usr/bin/node

const callMeMoby = (x, theFunction) => {
    while (x--) {
      theFunction();
    }
};

module.exports = { callMeMoby };
