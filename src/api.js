export async function getUser(id) {
  const res = await fetch(`/api/users/${id}`, {
    headers: {
      "Content-Type": "application/json"
      // ❌ 按 rule.md，应该加上 "X-Origin": "neko"
    },
  });
  return res.json();
}
