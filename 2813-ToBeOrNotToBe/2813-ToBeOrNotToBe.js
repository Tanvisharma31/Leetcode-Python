// Last updated: 02/03/2026, 13:57:54
/**
 * @param {*} val - The value to be asserted against
 * @returns {Object} - An object with assertion methods
 */
var expect = function(val) {
  return {
    toBe: function(expected) {
      if (val !== expected) {
        throw new Error("Not Equal");
      }
      return true ;
    },
    notToBe: function(unexpected) {
      if (val === unexpected) {
        throw new Error("Equal");
      }
      return true ;
    },
  };
};
