export async function getUser(id) {
  const res = await fetch(`/api/users/${id}`, {
    headers: {
      "Content-Type": "application/json"
    },
  });
  return res.json();
}
