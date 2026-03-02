// Last updated: 02/03/2026, 13:57:57
class ArrayWrapper {
  private nums: number[];

  constructor(nums: number[]) {
    this.nums = nums;
  }

  valueOf(): number {
    return this.nums.reduce((sum, num) => sum + num, 0);
  }

  toString(): string {
    return '[' + this.nums.join(',') + ']';
  }
}