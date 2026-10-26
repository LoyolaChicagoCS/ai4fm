(() => {
  const source = document.querySelector('.article-body .highlight-bibtex pre');
  const title = document.querySelector('.article-body h1');
  if (!source || !title) {
    return;
  }

  const bibtex = source.textContent.trim();
  const key = (bibtex.match(/@\w+\{([^,]+),/) || [])[1] || 'citation';

  const wrap = document.createElement('div');
  wrap.className = 'cite';
  wrap.innerHTML =
    '<button class="cite-toggle" type="button" aria-expanded="false" aria-controls="cite-panel">Cite</button>' +
    '<div class="cite-panel" id="cite-panel" hidden>' +
    '<pre class="cite-code" tabindex="0"></pre>' +
    '<div class="cite-actions">' +
    '<button class="cite-copy" type="button">Copy BibTeX</button>' +
    '<button class="cite-download" type="button">Download .bib</button>' +
    '<span class="cite-status" role="status" aria-live="polite"></span>' +
    '</div></div>';
  title.insertAdjacentElement('afterend', wrap);

  const toggle = wrap.querySelector('.cite-toggle');
  const panel = wrap.querySelector('.cite-panel');
  const status = wrap.querySelector('.cite-status');
  wrap.querySelector('.cite-code').textContent = bibtex;

  const say = (text) => {
    status.textContent = text;
    window.setTimeout(() => { status.textContent = ''; }, 2500);
  };

  toggle.addEventListener('click', () => {
    const open = panel.hidden;
    panel.hidden = !open;
    toggle.setAttribute('aria-expanded', String(open));
  });

  wrap.querySelector('.cite-copy').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(bibtex);
      say('Copied');
    } catch (error) {
      const range = document.createRange();
      range.selectNodeContents(wrap.querySelector('.cite-code'));
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      say('Press Ctrl+C or Cmd+C to copy');
    }
  });

  wrap.querySelector('.cite-download').addEventListener('click', () => {
    const url = URL.createObjectURL(new Blob([bibtex + '\n'], { type: 'text/plain' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = key + '.bib';
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
  });
})();
