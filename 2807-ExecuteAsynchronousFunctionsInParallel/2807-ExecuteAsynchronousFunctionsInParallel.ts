// Last updated: 02/03/2026, 13:57:56
type Fn<T> = () => Promise<T>;

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {
  return new Promise((resolve, reject) => {
    const ans: T[] = [];
    let resolveCount = 0;
    functions.forEach((fn, index) => {
      fn()
        .then((val) => {
          ans[index] = val;
          if (++resolveCount === functions.length) {
            resolve(ans);
          }
        })
        .catch((error) => {
          reject(error);
        });
    });
  });
}