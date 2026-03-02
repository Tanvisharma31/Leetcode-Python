// Last updated: 02/03/2026, 13:57:47
type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };
type Fn = (value: JSONValue) => number;

function sortBy(arr: JSONValue[], fn: Fn): JSONValue[] {
  arr.sort((a, b) => fn(a) - fn(b));
  return arr;
}