// Last updated: 02/03/2026, 13:58:07
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let counter = init; // Initialize the counter with the initial value
    
    return {
        increment: function() {
            return ++counter; // Increment the counter value and return it
        },
        decrement: function() {
            return --counter; // Decrement the counter value and return it
        },
        reset: function() {
            counter = init; // Reset the counter value to the initial value and return it
            return counter;
        }
    };
};


/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */