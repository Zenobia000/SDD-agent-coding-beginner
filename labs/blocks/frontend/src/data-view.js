/**
 * DataView —— 一個把「六種狀態」全部處理好的資料元件。
 *
 * 設計稿只會畫 Success 那一格。其餘五格是你的責任，
 * 而且它們才是使用者實際最常遇到的。
 *
 * 零依賴，原生 Web Component。對應 skill：/ui-spec
 *
 * 用法：
 *   <data-view id="rates"></data-view>
 *   const v = document.getElementById('rates');
 *   v.load(() => fetch('/api/rates').then(r => r.json()));
 */

export const STATES = Object.freeze({
  LOADING: 'loading',
  EMPTY: 'empty',
  ERROR: 'error',
  SUCCESS: 'success',
  PARTIAL: 'partial',
  FORBIDDEN: 'forbidden',
});

// 低於這個時間不顯示載入態 —— 否則畫面會閃一下，比沒有更糟
const LOADING_DELAY_MS = 300;

export class DataView extends HTMLElement {
  #state = STATES.LOADING;
  #data = [];
  #error = null;
  #loadingTimer = null;
  #retry = null;

  static get observedAttributes() {
    return ['empty-message', 'empty-action'];
  }

  connectedCallback() {
    this.#render();
  }

  /**
   * @param {() => Promise<{items: any[], hasMore?: boolean}>} fetcher
   */
  async load(fetcher) {
    this.#retry = () => this.load(fetcher);

    // 延遲顯示載入態：快的請求根本不會進入 loading，避免閃爍
    this.#loadingTimer = setTimeout(() => {
      this.#setState(STATES.LOADING);
    }, LOADING_DELAY_MS);

    try {
      const result = await fetcher();
      clearTimeout(this.#loadingTimer);

      if (result?.forbidden) {
        this.#setState(STATES.FORBIDDEN);
        return;
      }
      this.#data = result?.items ?? [];
      if (this.#data.length === 0) {
        this.#setState(STATES.EMPTY);
      } else if (result?.hasMore) {
        this.#setState(STATES.PARTIAL);
      } else {
        this.#setState(STATES.SUCCESS);
      }
    } catch (err) {
      clearTimeout(this.#loadingTimer);
      // 只留給使用者「發生什麼、能做什麼」，不要吐技術細節
      this.#error = err;
      this.#setState(STATES.ERROR);
    }
  }

  get state() {
    return this.#state;
  }

  #setState(next) {
    this.#state = next;
    this.#render();
    this.dispatchEvent(new CustomEvent('statechange', { detail: { state: next } }));
  }

  #render() {
    // aria-busy 讓螢幕閱讀器知道正在載入
    this.setAttribute('aria-busy', String(this.#state === STATES.LOADING));
    this.setAttribute('data-state', this.#state);
    this.innerHTML = this.#template();

    const retryBtn = this.querySelector('[data-action="retry"]');
    if (retryBtn) retryBtn.addEventListener('click', () => this.#retry?.());
  }

  #template() {
    switch (this.#state) {
      case STATES.LOADING:
        // 骨架屏的尺寸要接近成功態，否則載入完會跳版
        return `
          <div class="dv-skeleton" role="status" aria-label="載入中">
            <div class="dv-skeleton-row"></div>
            <div class="dv-skeleton-row"></div>
            <div class="dv-skeleton-row"></div>
          </div>`;

      case STATES.EMPTY:
        // 空狀態一定要給下一步，不要只說「沒有資料」
        return `
          <div class="dv-empty">
            <p>${this.getAttribute('empty-message') ?? '還沒有任何紀錄'}</p>
            ${
              this.getAttribute('empty-action')
                ? `<a class="dv-cta" href="${this.getAttribute('empty-action')}">建立第一筆</a>`
                : ''
            }
          </div>`;

      case STATES.ERROR:
        // 不只變紅：要有文字 + 圖示 + 可執行的動作。
        // 只用顏色傳達資訊，色盲使用者與螢幕閱讀器都拿不到。
        return `
          <div class="dv-error" role="alert">
            <span aria-hidden="true">⚠️</span>
            <p>載入失敗，可能是網路不穩。</p>
            <button type="button" data-action="retry" class="dv-retry">重試</button>
          </div>`;

      case STATES.FORBIDDEN:
        return `
          <div class="dv-forbidden" role="alert">
            <p>你沒有權限查看這份資料。</p>
          </div>`;

      case STATES.PARTIAL:
        return `${this.#rows()}
          <button type="button" data-action="retry" class="dv-more">載入更多</button>`;

      case STATES.SUCCESS:
      default:
        return this.#rows();
    }
  }

  #rows() {
    return `
      <ul class="dv-list">
        ${this.#data
          .map(
            (item) => `
          <li class="dv-item">
            <span class="dv-label" title="${escapeHtml(String(item.label ?? ''))}">${escapeHtml(
              String(item.label ?? '')
            )}</span>
            <span class="dv-value">${escapeHtml(String(item.value ?? ''))}</span>
          </li>`
          )
          .join('')}
      </ul>`;
  }
}

/** 一律跳脫。innerHTML + 未跳脫的外部資料 = XSS。 */
export function escapeHtml(str) {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

if (typeof customElements !== 'undefined' && !customElements.get('data-view')) {
  customElements.define('data-view', DataView);
}
