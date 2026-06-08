export const getChatResponse = async (question) => {
    const response = await fetch(
        `https://smarthealth-ai-1.onrender.com/api/chat/?question=${encodeURIComponent(question)}`
    );

    const data = await response.json();

    return data;
};