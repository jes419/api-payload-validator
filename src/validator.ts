export function isValidPayload(payload: unknown): boolean {
  return payload !== null && typeof payload === 'object';
}