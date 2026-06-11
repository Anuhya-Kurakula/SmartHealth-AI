export const getChatResponse = async (question) => {

  console.log("Question:", question);
  console.log("API URL:", import.meta.env.VITE_API_URL);

  const response = await fetch(
    `${import.meta.env.VITE_API_URL}/api/chat/?question=${encodeURIComponent(question)}`
  );

  const data = await response.json();

  console.log("Response:", data);

  return data;
};