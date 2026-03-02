// Last updated: 02/03/2026, 13:58:18
type F = (x: number) => number;

function compose(functions: F[]): F {
  return function (x) {
    return functions.reduceRight((val, f) => f(val), x);
  };
}