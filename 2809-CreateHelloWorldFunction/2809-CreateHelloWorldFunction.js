// Last updated: 02/03/2026, 13:57:55
/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    };
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */