export const saveToLocalStorage = (key, value) => {
  if (!key) {
    console.error('Key is required');
    return false;
  }
  if (!value) {
    console.error('Value is required');
    return false;
  }
  // console.log(key, value);
  
  try {
    localStorage.setItem(key, JSON.stringify(value));
  }
  catch (error) {
    console.error('Error saving to localStorage:', error);
    return false;
  }
  return true;
}

export const getFromLocalStorage = (key) => {
  if (!key) {
    console.error('Key is required');
    return null;
  }
  try {
    const value = localStorage.getItem(key);
    if (!value) {
      console.error('Value not found in localStorage', key);
      return null;
    }
    return JSON.parse(value);
  }
  catch (error) {
    console.error('Error getting from localStorage:', error);
    return null;
  }
}

export const removeFromLocalStorage = (key) => {
  if (!key) {
    console.error('Key is required');
    return false;
  }
  try {
    localStorage.removeItem(key);
  }
  catch (error) {
    console.error('Error removing from localStorage:', error);
    return false;
  }
  return true;
}

export const getUser = () => {
  const user = getFromLocalStorage('user');
  if (!user) {
    throw new Error('User not found in localStorage');
  }
  return user;
}


export const ClearLocalStorage = () => {
  localStorage.clear();
}
