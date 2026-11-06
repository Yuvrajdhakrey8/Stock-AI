/**
 * Checks whether Indian Equities Market (NSE & BSE) is currently open.
 * Standard Trading hours: Monday to Friday, 9:08 AM to 3:35 PM IST.
 * Excludes weekends (Saturday, Sunday).
 */
export function isIndianMarketOpen(): boolean {
  try {
    const now = new Date();
    // Convert local time to IST (UTC + 5.5 hours)
    const utc = now.getTime() + (now.getTimezoneOffset() * 60000);
    const istTime = new Date(utc + (3600000 * 5.5));

    const day = istTime.getDay(); // 0 = Sunday, 6 = Saturday
    if (day === 0 || day === 6) return false;

    const hours = istTime.getHours();
    const minutes = istTime.getMinutes();
    const totalMinutes = hours * 60 + minutes;

    // Active trading window: 9:08 AM (548) to 3:35 PM (935)
    return totalMinutes >= 548 && totalMinutes <= 935;
  } catch {
    return false;
  }
}

/**
 * Returns formatted IST market status text.
 */
export function getMarketStatus(): { isOpen: boolean; label: string } {
  const isOpen = isIndianMarketOpen();
  return {
    isOpen,
    label: isOpen ? 'Live Market' : 'Market Closed',
  };
}
