---
date: 2026-02-16
---

# Numbers 3

[Numbers 3 (BSB)](https://biblehub.com/bsb/numbers/3.htm)

<div id="camp-layout-wrap">
  <table id="camp-layout-table">
    <colgroup>
      <col span="5" style="width: 20%;" />
    </colgroup>
    <tr>
      <td class="empty"></td>
      <td><div id="tribe-benjamin" class="chart"></div></td>
      <td><div id="tribe-dan" class="chart"></div></td>
      <td><div id="tribe-asher" class="chart"></div></td>
      <td class="empty"></td>
    </tr>
    <tr>
      <td><div id="tribe-gad" class="chart"></div></td>
      <td class="empty"></td>
      <td><div id="levite-merari" class="chart"></div></td>
      <td class="empty"></td>
      <td><div id="tribe-naphtali" class="chart"></div></td>
    </tr>
    <tr>
      <td><div id="tribe-ephraim" class="chart"></div></td>
      <td><div id="levite-gershon" class="chart"></div></td>
      <td class="tent-cell"><div id="tent-label">Tent of Meeting</div></td>
      <td><div id="levite-aaron-moses" class="chart"></div></td>
      <td><div id="tribe-judah" class="chart"></div></td>
    </tr>
    <tr>
      <td><div id="tribe-manasseh" class="chart"></div></td>
      <td class="empty"></td>
      <td><div id="levite-kohath" class="chart"></div></td>
      <td class="empty"></td>
      <td><div id="tribe-issachar" class="chart"></div></td>
    </tr>
    <tr>
      <td class="empty"></td>
      <td><div id="tribe-zebulun" class="chart"></div></td>
      <td><div id="tribe-reuben" class="chart"></div></td>
      <td><div id="tribe-simeon" class="chart"></div></td>
      <td class="empty"></td>
    </tr>
  </table>
</div>

<style>
  #camp-layout-wrap {
    width: 100%;
    max-width: 980px;
    margin: 1rem auto;
  }
  #camp-layout-table {
    width: 100%;
    height: min(980px, 100vw);
    table-layout: fixed;
    border-collapse: collapse;
    border: 0;
    background: transparent;
  }
  #camp-layout-table td {
    border: 0;
    background: transparent;
    padding: 4px;
    width: 20%;
    height: 160px;
    vertical-align: middle;
  }
  #camp-layout-table tr:hover,
  #camp-layout-table td:hover {
    background: transparent;
  }
  .chart {
    width: 100%;
    height: 100%;
    min-height: 140px;
  }
  .empty {
    background: transparent;
  }
  .tent-cell {
    text-align: center;
  }
  #tent-label {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    border-radius: 999px;
    border: 2px solid #8a6d1f;
    background: #f8f1dc;
    color: #5a4713;
    font-weight: 700;
    font-size: 12px;
    letter-spacing: 0.02em;
  }

  @media (max-width: 900px) {
    #camp-layout-table,
    #camp-layout-table tbody,
    #camp-layout-table tr,
    #camp-layout-table td {
      display: block;
      width: 100%;
      height: auto;
    }
    .empty {
      display: none !important;
    }
    .chart,
    #tent-label {
      height: 210px;
      min-height: 210px;
      margin-bottom: 0.75rem;
    }
  }
</style>

<script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
<script>
  const fmt = (n) => Math.abs(n).toLocaleString();
  const SHARED_MAX = 80000;

  function barLabel(color = "#111") {
    return {
      show: true,
      position: "inside",
      formatter: (p) => `${p.name}\n${fmt(p.value)}`,
      color,
      fontWeight: "bold",
      fontSize: 11,
      lineHeight: 13
    };
  }

  function verticalBar(id, name, value, color, opts = {}) {
    const chart = echarts.init(document.getElementById(id));
    chart.setOption({
      animation: false,
      grid: { left: 0, right: 0, top: 0, bottom: 0 },
      xAxis: { type: "category", data: [name], show: false },
      yAxis: {
        type: "value",
        min: 0,
        max: SHARED_MAX,
        inverse: Boolean(opts.down),
        show: false
      },
      series: [{
        type: "bar",
        barWidth: "78%",
        data: [{ value, name, itemStyle: { color, borderColor: opts.borderColor, borderWidth: opts.borderWidth ?? 0 } }],
        label: barLabel(opts.labelColor)
      }]
    });
    return chart;
  }

  function horizontalBar(id, name, value, color, opts = {}) {
    const chart = echarts.init(document.getElementById(id));
    chart.setOption({
      animation: false,
      grid: { left: 0, right: 0, top: 0, bottom: 0 },
      xAxis: {
        type: "value",
        min: 0,
        max: SHARED_MAX,
        inverse: Boolean(opts.reverse),
        show: false
      },
      yAxis: { type: "category", data: [name], show: false },
      series: [{
        type: "bar",
        barWidth: "78%",
        data: [{ value, name, itemStyle: { color, borderColor: opts.borderColor, borderWidth: opts.borderWidth ?? 0 } }],
        label: barLabel(opts.labelColor)
      }]
    });
    return chart;
  }

  const charts = [
    verticalBar("tribe-benjamin", "Benjamin", 35400, "#c04000", { labelColor: "#fff" }),
    verticalBar("tribe-dan", "Dan", 62700, "#0f52ba", { labelColor: "#fff" }),
    verticalBar("tribe-asher", "Asher", 41500, "#9a7b4f", { labelColor: "#fff" }),

    horizontalBar("tribe-gad", "Gad", 45650, "#d73b3e", { reverse: true, labelColor: "#fff" }),
    horizontalBar("tribe-ephraim", "Ephraim", 40500, "#353839", { reverse: true, labelColor: "#fff" }),
    horizontalBar("tribe-manasseh", "Manasseh", 32200, "#7a7d80", { reverse: true, labelColor: "#fff" }),

    horizontalBar("tribe-naphtali", "Naphtali", 53400, "#eaf6ff", { borderColor: "#a8b9cc", borderWidth: 1 }),
    horizontalBar("tribe-judah", "Judah", 74600, "#40e0d0"),
    horizontalBar("tribe-issachar", "Issachar", 54400, "#9966cc", { labelColor: "#fff" }),

    verticalBar("tribe-zebulun", "Zebulun", 57400, "#7fffd4", { down: true }),
    verticalBar("tribe-reuben", "Reuben", 46500, "#e0115f", { down: true, labelColor: "#fff" }),
    verticalBar("tribe-simeon", "Simeon", 59300, "#ffc87c", { down: true }),

    verticalBar("levite-merari", "Merari", 6200, "#8c6239", { labelColor: "#fff" }),
    horizontalBar("levite-gershon", "Gershon", 7500, "#d4af37", { reverse: true }),
    horizontalBar("levite-aaron-moses", "Aaron+Moses", 2, "#f8e7b2"),
    verticalBar("levite-kohath", "Kohath", 8600, "#b08d57", { down: true })
  ];

  window.addEventListener("resize", () => charts.forEach((c) => c.resize()));
</script>
