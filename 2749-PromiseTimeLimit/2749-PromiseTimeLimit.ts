// Last updated: 02/03/2026, 13:58:12
type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
  return async function (...args) {
    const p1 = new Promise((_, reject) => {
      setTimeout(() => reject('Time Limit Exceeded'), t);
    });
    const p2 = fn(...args);
    return Promise.race([p1, p2]);
  };
}