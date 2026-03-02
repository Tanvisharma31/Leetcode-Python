// Last updated: 02/03/2026, 13:57:51
type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => void;

function cancellable(fn: Fn, args: JSONValue[], t: number): Function {
  const timer = setTimeout(() => fn(...args), t);
  return function () {
    clearTimeout(timer);
  };
}