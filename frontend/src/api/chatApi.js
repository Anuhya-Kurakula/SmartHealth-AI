export const getChatResponse = async (question) => {
  const response = await fetch(
    `${import.meta.env.VITE_API_URL}/api/chat/?question=${encodeURIComponent(question)}`
  );

  return await response.json();
};