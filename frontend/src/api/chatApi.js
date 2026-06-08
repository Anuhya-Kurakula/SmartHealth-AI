export const getChatResponse = async () => {
    const response = await fetch(
        "https://smarthealth-ai-1.onrender.com/api/chat/"
    );

    const data = await response.json();

    return data;
};