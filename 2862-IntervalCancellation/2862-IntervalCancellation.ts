// Last updated: 02/03/2026, 13:57:46
type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void;

function cancellable(fn: Fn, args: JSONValue[], t: number): Function {
  fn(...args);
  const timer = setInterval(() => fn(...args), t);
  return function () {
    clearInterval(timer);
  };
}