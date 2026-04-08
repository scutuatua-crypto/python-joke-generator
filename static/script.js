/**
 * Joke Generator – frontend script
 * Fetches jokes from the Flask /api/joke endpoint and updates the UI.
 */

const jokeContent     = document.getElementById('joke-content');
const loadingEl       = document.getElementById('loading');
const errorEl         = document.getElementById('error-message');
const jokeBtn         = document.getElementById('joke-btn');
const categoryBadgeRow = document.getElementById('category-badge-row');
const categoryBadge   = document.getElementById('category-badge');
const sourceBadge     = document.getElementById('source-badge');

function setLoading(isLoading) {
  jokeBtn.disabled = isLoading;
  loadingEl.classList.toggle('hidden', !isLoading);
  jokeContent.classList.toggle('hidden', isLoading);
  categoryBadgeRow.style.display = isLoading ? 'none' : '';
  errorEl.classList.add('hidden');
}

function showError(message) {
  errorEl.querySelector('span').textContent = '⚠️ ' + (message || 'Something went wrong. Please try again.');
  errorEl.classList.remove('hidden');
  jokeContent.innerHTML = '';
  categoryBadgeRow.style.display = 'none';
}

function renderJoke(joke) {
  jokeContent.classList.remove('fade-in');
  // Trigger reflow to restart animation
  void jokeContent.offsetWidth;

  if (joke.type === 'single') {
    jokeContent.innerHTML = `<p class="joke-single">${escapeHtml(joke.joke)}</p>`;
  } else if (joke.type === 'twopart') {
    jokeContent.innerHTML =
      `<p class="joke-setup">${escapeHtml(joke.setup)}</p>` +
      `<p class="joke-delivery">${escapeHtml(joke.delivery)}</p>`;
  } else {
    jokeContent.innerHTML = `<p class="joke-single">${escapeHtml(joke.joke || joke.setup || '')}</p>`;
  }

  jokeContent.classList.add('fade-in');

  // Update badges
  if (joke.category) {
    categoryBadge.textContent = joke.category;
    categoryBadge.style.display = '';
  } else {
    categoryBadge.style.display = 'none';
  }

  sourceBadge.textContent = joke.source === 'fallback' ? '📦 offline' : '🌐 live';
  categoryBadgeRow.style.display = 'flex';
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

async function fetchJoke() {
  setLoading(true);
  try {
    const response = await fetch('/api/joke');
    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }
    const data = await response.json();
    if (data && data.joke) {
      renderJoke(data.joke);
    } else {
      showError('Received an unexpected response. Please try again.');
    }
  } catch (err) {
    showError('Could not reach the server. Please check your connection.');
    console.error('Joke fetch error:', err);
  } finally {
    setLoading(false);
  }
}

// Fetch a joke on page load
window.addEventListener('DOMContentLoaded', fetchJoke);
